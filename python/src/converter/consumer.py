import pika, sys, os, time
from pymongo import MongoClient
import gridfs
from convert import to_mps

def main():
    client = MongoClient('host.minikube.internal', 27017)
    db_videos = client.videos
    db_mp3s = client.mp3s
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_mp3s)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.basic_consume()