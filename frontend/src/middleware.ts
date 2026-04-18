import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

// Mapeamento de rotas que requerem login
const protectedRoutes = ['/dashboard'];
// Rotas de autenticação (não acessíveis se já estiver logado)
const authRoutes = ['/login', '/register'];

export function middleware(request: NextRequest) {
  const token = request.cookies.get('access_token')?.value;
  const path = request.nextUrl.pathname;

  const isProtectedRoute = protectedRoutes.some((route) => path.startsWith(route));
  const isAuthRoute = authRoutes.includes(path);

  // Se não tem token e a rota é protegida => redirecionar para /login
  if (!token && isProtectedRoute) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Se tem token e tenta acessar /login ou /register => redirecionar para /dashboard
  if (token && isAuthRoute) {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }

  return NextResponse.next();
}

// Configuração do matcher (em quais caminhos o middleware deve rodar)
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
