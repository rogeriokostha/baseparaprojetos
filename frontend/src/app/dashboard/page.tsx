"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { clearAuthCookies } from "@/actions/auth";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { LogOut, User as UserIcon, LayoutDashboard, Settings } from "lucide-react";
import Link from "next/link";
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { api } from "@/lib/api";

export default function DashboardPage() {
  const router = useRouter();
  const [loadingLogout, setLoadingLogout] = useState(false);

  // Exemplo de logout usando a server action
  const handleLogout = async () => {
    setLoadingLogout(true);
    await clearAuthCookies();
    // A própria server action fará o redirect para /login, mas podemos forçar tbm:
    router.push("/login");
  };

  return (
    <div className="flex min-h-screen bg-black text-slate-50 selection:bg-indigo-500/30">
      {/* Sidebar Simples */}
      <aside className="w-64 border-r border-white/10 hidden md:flex flex-col bg-slate-950/30">
        <div className="h-20 flex items-center px-6 border-b border-white/10">
          <span className="font-bold text-xl tracking-tighter text-indigo-400">
            Dev Imortal
          </span>
        </div>
        <nav className="flex-1 p-4 space-y-2">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2 bg-indigo-600/10 text-indigo-400 rounded-md transition-colors">
            <LayoutDashboard className="h-5 w-5" />
            <span className="font-medium">Visão Geral</span>
          </Link>
          <Link href="#" className="flex items-center gap-3 px-3 py-2 text-slate-400 hover:text-slate-100 hover:bg-white/5 rounded-md transition-colors">
            <UserIcon className="h-5 w-5" />
            <span className="font-medium">Perfil</span>
          </Link>
          <Link href="#" className="flex items-center gap-3 px-3 py-2 text-slate-400 hover:text-slate-100 hover:bg-white/5 rounded-md transition-colors">
            <Settings className="h-5 w-5" />
            <span className="font-medium">Configurações</span>
          </Link>
        </nav>
        <div className="p-4 border-t border-white/10">
          <Button 
            variant="ghost" 
            className="w-full justify-start text-red-400 hover:text-red-300 hover:bg-red-950/30"
            onClick={handleLogout}
            disabled={loadingLogout}
          >
            <LogOut className="h-5 w-5 mr-3" />
            Sair
          </Button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col">
        <header className="h-20 flex items-center justify-between px-6 border-b border-white/10 bg-black/50 backdrop-blur-md sticky top-0">
          <div className="font-semibold text-lg md:hidden">Dev Imortal</div>
          <div className="ml-auto flex items-center gap-4">
            <div className="h-8 w-8 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 flex items-center justify-center text-sm font-bold shadow-lg">
              UD
            </div>
          </div>
        </header>

        <div className="flex-1 p-6 lg:p-10">
          <div className="max-w-5xl mx-auto space-y-8">
            <div>
              <h1 className="text-3xl font-bold tracking-tight">Visão Geral</h1>
              <p className="text-slate-400 mt-1">Bem-vindo à sua área protegida após o login.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              <Card className="bg-slate-950/50 border-white/10 backdrop-blur-md">
                <CardHeader className="pb-2">
                  <CardDescription className="text-slate-400">Total de Projetos</CardDescription>
                  <CardTitle className="text-3xl text-white">12</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-xs text-emerald-400 font-medium">+2 esse mês</p>
                </CardContent>
              </Card>

              <Card className="bg-slate-950/50 border-white/10 backdrop-blur-md">
                <CardHeader className="pb-2">
                  <CardDescription className="text-slate-400">Requisições JWT</CardDescription>
                  <CardTitle className="text-3xl text-white">4.3k</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-xs text-indigo-400 font-medium">Autenticação funcionando perfeitamente</p>
                </CardContent>
              </Card>
            </div>
            
            <div className="rounded-xl border border-white/10 bg-slate-950/30 p-8 text-center mt-12">
              <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-emerald-500/10 mb-4">
                <UserIcon className="h-8 w-8 text-emerald-400" />
              </div>
              <h3 className="text-xl font-bold text-white mb-2">Login Efetuado com Sucesso</h3>
              <p className="text-slate-400 max-w-md mx-auto">
                Este conteúdo está bloqueado nativamente pelo Next.js (Middleware) e só é renderizado porque você possui os cookies HTTPOnly gerados no momento do Login.
              </p>
            </div>
            
          </div>
        </div>
      </main>
    </div>
  );
}
