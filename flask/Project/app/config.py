# DB CONNECTION

conf={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
}


class Config:
    SQLALCHEMY_DATABASE_URI=f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:5432/postgres"