from flask import Flask,render_template,redirect,url_for
import sqlite3
app=Flask(__name__)
posts=[]
