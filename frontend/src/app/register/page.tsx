"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { api } from "@/lib/api";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import Link from "next/link";
import { Loader2 } from "lucide-react";

// Adapte o schema caso seu backend também exija username e afins
const registerSchema = z.object({
  email: z.string().email("Insira um email válido"),
  password: z.string().min(8, "A senha deve ter no mínimo 8 caracteres"),
  confirmPassword: z.string()
}).refine((data) => data.password === data.confirmPassword, {
  message: "As senhas não coincidem",
  path: ["confirmPassword"],
});

type RegisterForm = z.infer<typeof registerSchema>;

export default function RegisterPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterForm>({
    resolver: zodResolver(registerSchema),
  });

  const onSubmit = async (data: RegisterForm) => {
    setError(null);
    try {
      // Chamada para a API do Django dj-rest-auth para registrar
      await api.post("/auth/register/", {
        email: data.email,
        username: data.email, // Fallback p/ username se o django default user model exigir
        password: data.password,
        password1: data.password, // dj-rest-auth usa password1 e password0 as vezes
        password2: data.confirmPassword,
      });

      // Se der certo, redirecionamos para login (já que algumas APIs exigem opt-in ou verificação)
      router.push("/login?registered=true");
    } catch (err: any) {
      if (err.response?.data) {
        // Formatar erros do backend drf simplificados
        const errorMessages = Object.values(err.response.data).flat().join(" ");
        setError(errorMessages || "Erro ao registrar. Tente novamente.");
      } else {
        setError("Erro de rede. Tente mais tarde.");
      }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black p-4 selection:bg-indigo-500/30">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-indigo-900/20 via-black to-black -z-10" />
      
      <Card className="w-full max-w-md bg-slate-950/50 border-white/10 backdrop-blur-xl shadow-2xl">
        <CardHeader className="space-y-2 text-center pb-6">
          <CardTitle className="text-3xl font-bold tracking-tight text-white">Criar Conta</CardTitle>
          <CardDescription className="text-slate-400">Junte-se ao Boilerplate Definitivo</CardDescription>
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
              <Label htmlFor="password" className="text-slate-200">Senha</Label>
              <Input
                id="password"
                type="password"
                className="bg-black/50 border-white/10 text-white focus-visible:ring-indigo-500"
                {...register("password")}
              />
              {errors.password && <p className="text-sm text-red-500">{errors.password.message}</p>}
            </div>

            <div className="space-y-2">
              <Label htmlFor="confirmPassword" className="text-slate-200">Confirmar Senha</Label>
              <Input
                id="confirmPassword"
                type="password"
                className="bg-black/50 border-white/10 text-white focus-visible:ring-indigo-500"
                {...register("confirmPassword")}
              />
              {errors.confirmPassword && <p className="text-sm text-red-500">{errors.confirmPassword.message}</p>}
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
              {isSubmitting ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : "Finalizar Cadastro"}
            </Button>
          </form>
        </CardContent>
        <CardFooter className="flex justify-center border-t border-white/10 pt-6">
          <p className="text-sm text-slate-400">
            Já possui uma conta?{" "}
            <Link href="/login" className="text-indigo-400 hover:text-indigo-300 font-medium">
              Faça login
            </Link>
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}
