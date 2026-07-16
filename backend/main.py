from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def root(): return {'name':'Chenar AI','version':'0.1'}
