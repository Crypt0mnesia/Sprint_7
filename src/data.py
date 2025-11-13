
class StatusCodes:
    SUCCESS_CREATION = 201
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class ResponseMessages:
    CREATION_SUCCESS = {"ok": True}
    INSUFFICIENT_DATA_CREATION = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"
    }
    INSUFFICIENT_DATA_LOGIN = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }
    LOGIN_ALREADY_EXISTS = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."
    }
    ACCOUNT_NOT_FOUND = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }


class ExpectedResponses:
    # Для создания курьера
    SUCCESSFUL_CREATION = (StatusCodes.SUCCESS_CREATION, ResponseMessages.CREATION_SUCCESS)
    DUPLICATE_COURIER = (StatusCodes.CONFLICT, ResponseMessages.LOGIN_ALREADY_EXISTS)
    MISSING_REQUIRED_FIELD = (StatusCodes.BAD_REQUEST, ResponseMessages.INSUFFICIENT_DATA_CREATION)

    # Для логина курьера
    SUCCESSFUL_LOGIN = (StatusCodes.SUCCESS, None)  # Тело проверяется отдельно на наличие id
    MISSING_LOGIN_FIELD = (StatusCodes.BAD_REQUEST, ResponseMessages.INSUFFICIENT_DATA_LOGIN)
    ACCOUNT_NOT_FOUND = (StatusCodes.NOT_FOUND, ResponseMessages.ACCOUNT_NOT_FOUND)

    # Для заказов
    SUCCESSFUL_ORDER_CREATION = (StatusCodes.SUCCESS_CREATION, None)  # Тело проверяется на наличие track
    SUCCESSFUL_ORDER_LIST = (StatusCodes.SUCCESS, None)