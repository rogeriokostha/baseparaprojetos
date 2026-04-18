import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-black text-slate-50 selection:bg-indigo-500/30">
      <header className="flex h-20 items-center px-6 lg:px-12 backdrop-blur-md border-b border-white/10 sticky top-0 z-50">
        <Link className="flex items-center justify-center" href="#">
          <span className="font-bold text-2xl tracking-tighter bg-gradient-to-r from-blue-400 to-indigo-500 bg-clip-text text-transparent">
            Dev Imortal
          </span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6 items-center">
          <Link className="text-sm font-medium hover:text-indigo-400 transition-colors" href="#">
            Features
          </Link>
          <Link className="text-sm font-medium hover:text-indigo-400 transition-colors" href="#">
            Preços
          </Link>
          <div className="h-6 w-px bg-white/20 mx-2" />
          <Link href="/login">
            <Button variant="ghost" className="text-slate-50 hover:text-white hover:bg-white/10">Entrar</Button>
          </Link>
          <Link href="/register">
            <Button className="bg-indigo-600 text-white hover:bg-indigo-500">Começar</Button>
          </Link>
        </nav>
      </header>
      <main className="flex-1 flex flex-col items-center justify-center p-6 text-center">
        <div className="space-y-6 max-w-[800px]">
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tighter">
            O Boilerplate <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500">
              Definitivo
            </span>
          </h1>
          <p className="text-xl text-slate-400 max-w-[600px] mx-auto leading-relaxed">
            Comece seus projetos voando. Autenticação JWT, banco de dados isolado e componentes premium fora da caixa.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
            <Link href="/register">
              <Button size="lg" className="h-12 px-8 text-base bg-indigo-600 hover:bg-indigo-500 shadow-[0_0_40px_-10px_rgba(79,70,229,0.5)]">
                Criar Conta Agora
              </Button>
            </Link>
            <Link href="/login">
              <Button size="lg" variant="outline" className="h-12 px-8 text-base border-white/20 text-slate-300 hover:bg-white/10 hover:text-white">
                Acessar Painel
              </Button>
            </Link>
          </div>
        </div>
      </main>
      <footer className="py-6 w-full shrink-0 items-center px-4 md:px-6 border-t border-white/10">
        <p className="text-xs text-slate-500 text-center">
          © 2026 Dev Imortal Boilerplate. Todos os direitos reservados.
        </p>
      </footer>
    </div>
  );
}
