"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { api } from "@/lib/api";
import { setAuthCookies } from "@/actions/auth";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import Link from "next/link";
import { Loader2 } from "lucide-react";

const loginSchema = z.object({
  email: z.string().email("Insira um email válido"),
  password: z.string().min(1, "A senha é obrigatória"),
});

type LoginForm = z.infer<typeof loginSchema>;

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginForm) => {
    setError(null);
    try {
      // Usando dj-rest-auth ou simplejwt, variaveis podem divergir, assumindo username/password fallback ou email/password
      const res = await api.post("/auth/login/", {
        username: data.email, // Depende do adapter JWT do Django (geralmente mapeia email -> username)
        email: data.email,
        password: data.password,
      });

      const { access, refresh } = res.data;
      if (access && refresh) {
        await setAuthCookies(access, refresh);
        router.push("/dashboard");
      }
    } catch (err: any) {
      if (err.response?.data?.detail) {
        setError(err.response.data.detail);
      } else {
        setError("Credenciais inválidas ou erro no servidor");
      }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black p-4 selection:bg-indigo-500/30">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-indigo-900/20 via-black to-black -z-10" />
      
      <Card className="w-full max-w-md bg-slate-950/50 border-white/10 backdrop-blur-xl shadow-2xl">
        <CardHeader className="space-y-2 text-center pb-6">
          <CardTitle className="text-3xl font-bold tracking-tight text-white">Bem-vindo de volta</CardTitle>
          <CardDescription className="text-slate-400">Entre na sua conta para continuar</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email" className="text-slate-200">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="nome@exemplo.com"
                className="bg-black/50 border-white/10 text-white placeholder:text-slate-600 focus-visible:ring-indigo-500"
                {...register("email")}
              />
              {errors.email && <p className="text-sm text-red-500">{errors.email.message}</p>}
            </div>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label htmlFor="password" className="text-slate-200">Senha</Label>
                <Link href="#" className="text-sm text-indigo-400 hover:text-indigo-300">
                  Esqueceu a senha?
                </Link>
              </div>
              <Input
                id="password"
                type="password"
                className="bg-black/50 border-white/10 text-white focus-visible:ring-indigo-500"
                {...register("password")}
              />
              {errors.password && <p className="text-sm text-red-500">{errors.password.message}</p>}
            </div>

            {error && (
              <div className="p-3 rounded-md bg-red-500/10 border border-red-500/20 text-red-400 text-sm">
                {error}
              </div>
            )}

            <Button
              type="submit"
              className="w-full bg-indigo-600 hover:bg-indigo-500 text-white mt-6 h-11"
              disabled={isSubmitting}
            >
              {isSubmitting ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : "Entrar"}
            </Button>
          </form>
        </CardContent>
        <CardFooter className="flex justify-center border-t border-white/10 pt-6">
          <p className="text-sm text-slate-400">
            Não tem uma conta?{" "}
            <Link href="/register" className="text-indigo-400 hover:text-indigo-300 font-medium">
              Registre-se
            </Link>
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}
