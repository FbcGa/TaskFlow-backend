import os

bind = "0.0.0.0:{}".format(os.getenv("PORT", 3001))
workers = 3  # Puedes ajustar según tus necesidades
timeout = 120  # Aumenta el tiempo de espera si es necesario
