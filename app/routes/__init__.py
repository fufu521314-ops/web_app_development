from .main import bp as main_bp
from .auth import bp as auth_bp
from .fortune import bp as fortune_bp
from .history import bp as history_bp
from .payment import bp as payment_bp

__all__ = [
    'main_bp',
    'auth_bp',
    'fortune_bp',
    'history_bp',
    'payment_bp'
]
