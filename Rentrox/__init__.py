import os
from os import getenv
import logging

class Config:
    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = getenv("BOT_TOKEN", "5852732942:AAGNiEPl6yNKoOBQdLogyaABecPHHMj8ObU")
    BOT_SESSION = "bot" 
    FROM_CHANNEL = -1001667023505 #https://t.me/ ccgfdjhdjjgdsd
    FILTER_TYPE = "document"
    OWNER_ID = "5163706369"
    SESSION = getenv("SESSION", "BQFR5_YAJSXOivoI3mUhR8xc75P8ejYMemW-l49tw2BEgnIwdrTVcuM0lnLT8hhkmIBZ8y3Nolhz7XmCvI38hk0Uiyq6BwmpUIuNORAMlfl4yfWMxmOpf41QDjOlw6cn6TRA-5hB3twBoRXxL1_bEUDWgJhCQgd-8LKYTJnGQdB3mJc_u3CY4e-FJCjzIv5NNL_XWlDwo_BczqhLr5Fas_3j6WqnaFo8KHXuycRJrR2NxQ0GdaeIaTiJnaDVUUnIHKnIxH7PqyBZtIv3-F6VeqwlStF47TjebzYLK_gHlkHGa6N8aGVIyZbxpck1nT5a-LcOKYtvdRH3NB94T8jObE0F89DdkAAAAAFluR1oAA")
    TO_CHANNEL = -1001925446238    
#    FILTERGROUP_1_ID = -1001589825618
#    FILTERGROUP_2_ID = -1001556192813
    SEARCHCHANNEL_ID = -1001556192813
    ADMINS = [5163706369, 'TheLx0980', 1533128706]
    GROUPS = [-1001556192813, -1001589825618, -1001985927263]

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
