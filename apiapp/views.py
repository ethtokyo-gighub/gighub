# http
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from datetime import datetime

# apiapp
from .models import *
from .serializers import *

# rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

# swagger-openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# signin

# display loans list
@swagger_auto_schema(method='get', responses={200: LoanSerializer(many=True)})
@api_view(['GET'])
@permission_classes([AllowAny])
def loan_list(request):
    loans = Loan.objects.filter(user=request.user.id)
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)

# display loan detail
@swagger_auto_schema(method='get', responses={200: LoanSerializer()})
@api_view(['GET'])
@permission_classes([AllowAny])
def loan_detail(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    serializer = LoanSerializer(loan)
    return Response(serializer.data)

# apply loan - update loan object
@swagger_auto_schema(method='put', request_body=LoanSerializer, responses={200: LoanSerializer()})
@api_view(['PUT'])
@permission_classes([AllowAny])
def loan_update(self, request, pk):
    data = request.DATA
    loan = get_object_or_404(Loan, pk=pk)
    serializer = LoanSerializer(data=data, many=True)

    max_borrowing_amount = loan.user.wage*0.3
    duration = 20
    org_title = loan.organization.title
    loan.accrued_interest = duration*(loan.APR/365)*loan.borrowing_amount

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# apply for a loan 

# apply for a loan - update loan item
# max_borrowing_amount = next_paycheck_amount*0.3
# duration = next_paycheck_date - loan_date
# accrued_interest = duration*APR/365*borrowing_amount

# dashboard
#  total_borrowing_amount = 
# 

# take loan - createview
