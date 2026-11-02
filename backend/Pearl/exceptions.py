class PearlError(Exception):
    """
    Base exception for the Pearl domain
    """
    pass

class InvalidCaptureRequest(PearlError):
    """Raised when a capture request violates the Pearl capture contract"""
    pass

class UnknownSourceType(Exception):
    '''
    Raised when sourcetype is not known
    '''
    pass