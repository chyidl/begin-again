from concurrent import futures
import random
import grpc
from recommendations_pb2 import BookCategory, BookRecommendation, RecommendationResponse
import recommendations_pb2_grpc


books_by_category = {
    BookCategory.MYSTERY: [BookRecommendation(id=1, title="The Maltese Falcon"), BookRecommendation(id=2, title="Mu")]
}