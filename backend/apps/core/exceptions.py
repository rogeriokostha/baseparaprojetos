from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return response

    status_code = response.status_code
    detail = response.data

    message = "Erro na requisição."
    errors = None

    if status_code == 400:
        message = "Dados inválidos."
        errors = detail

    elif status_code == 401:
        message = "Você precisa estar autenticado para acessar este recurso."

    elif status_code == 403:
        message = "Você não tem permissão para executar esta ação."

    elif status_code == 404:
        message = "Recurso não encontrado."

    elif status_code >= 500:
        message = "Erro interno do servidor."

    response.data = {
        "success": False,
        "status_code": status_code,
        "message": message,
        "errors": errors,
    }

    return response