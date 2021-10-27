"""Exceptions raised by the Directory Service service."""
from moto.core.exceptions import JsonRESTError


class DsValidationException(JsonRESTError):
    """Report one of more parameter validation errors."""

    code = 400

    def __init__(self, error_tuples):
        """Validation errors are concatenated into one exception message.

        error_tuples is a list of tuples.  Each tuple contains:

          - name of invalid parameter,
          - value of invalid parameter,
          - string describing the constraints for that parameter.
        """
        msg_leader = (
            f"{len(error_tuples)} "
            f"validation error{'s' if len(error_tuples) > 1 else ''} detected: "
        )
        msgs = []
        for arg_name, arg_value, constraint in error_tuples:
            value = "at" if arg_name == "password" else f"'{arg_value}' at"
            msgs.append(
                f"Value {value} '{arg_name}' failed to satisfy constraint: "
                f"Member must {constraint}"
            )
        super().__init__("ValidationException", msg_leader + "; ".join(msgs))


class ClientException(JsonRESTError):
    """Client exception has occurred. VPC parameters are invalid."""

    code = 400

    def __init__(self, message):
        super().__init__("ClientException", message)


class DirectoryLimitExceededException(JsonRESTError):
    """Maximum number of directories in region has been reached."""

    code = 400

    def __init__(self, message):
        super().__init__("DirectoryLimitExceededException", message)


class InvalidParameterException(JsonRESTError):
    """Invalid parameter."""

    code = 400

    def __init__(self, message):
        super().__init__("InvalidParameterException", message)
