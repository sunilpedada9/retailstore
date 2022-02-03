from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from store import item_serializer
from store import category_serializer
from store.category_serializer import CategorySerializer
from store.item_serializer import ItemSerializer
from store.rack_serializer import RackSerializer
from helper.utils import get_pagination
from .models import Category, Item, Rack
from django.db.models import Q
from rest_framework import serializers, status
# Create your views here.

# Create category 
class CategoryCreate(CreateAPIView):
    serializer_class=CategorySerializer

# Get category list or remove category
class CategoryListAndRemove(APIView):
    def get(self,request):
        sort_by=self.request.GET.get("sort_by")
        sort_type=self.request.GET.get("sort_type")
        per_page_rows=self.request.GET.get("per_page_items")
        page_no=self.request.GET.get("page_no")
        category_name=self.request.GET.get("category_name")
        search=''
        if category_name:
            search+=' and category_name={}'.format(category_name)
        if sort_by:
            search+=' order by {}'.format(sort_by)
        if not sort_by:
            search+=' order by id'
        if sort_type:
            search+=' {}'.format(sort_type)
        if not per_page_rows or not page_no:
            per_page_rows=None
            page_no=None
        if per_page_rows:
            per_page_rows=int(per_page_rows)
        if page_no:
            page_no=int(page_no)
        pagination=get_pagination(per_page_rows=per_page_rows,page_no=page_no)
        print(pagination)
        category_data=Category.objects.raw("""select * from store_category where status_id != '3'{search} 
                                                limit {offset},{limit};""".format(
                                                    search=search,offset=pagination["offset"],limit=pagination["limit"]
                                                ))
        print(category_data)
        serialized_data=CategorySerializer(category_data,many=True)
        print(serialized_data.data)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    def delete(self,request):
        try:
            id=self.request.data["id"]
            delete_status=Category.objects.get(Q(id=id) & ~Q(status_id=3))
            delete_status.status_id=3
            delete_status.save()
            return Response({"message":"Successfully removed."},status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist:
            return Response({"message":"Category not exist!."},status=status.HTTP_200_OK)
        
# Add items
class CreateItem(CreateAPIView):
    serializer_class=ItemSerializer

# List,update and remove item
class ListUpdateRemoveItem(APIView):
    def get(self,request):
        sort_by=self.request.GET.get("sort_by")
        sort_type=self.request.GET.get("sort_type")
        per_page_rows=self.request.GET.get("per_page_items")
        page_no=self.request.GET.get("page_no")
        item_name=self.request.GET.get("item_name")
        search=''
        if item_name:
            search+=' and item_name={}'.format(item_name)
        if sort_by:
            search+=' order by {}'.format(sort_by)
        if not sort_by:
            search+=' order by id'
        if sort_type:
            search+=' {}'.format(sort_type)
        print("ff",page_no,per_page_rows)
        if per_page_rows:
            per_page_rows=int(per_page_rows)
        if page_no:
            page_no=int(page_no)
        if not per_page_rows:
            per_page_rows=None
        if not page_no:
            page_no=None
        print(page_no,per_page_rows)
        pagination=get_pagination(per_page_rows=per_page_rows,page_no=page_no)
        print(pagination)
        item_name=(~Q(status_id=3) & Q(item_name=item_name)) if item_name else (~Q(status_id=3))
        sort_by=sort_by.lower() if sort_by else 'id' 
        sort_by='-' + sort_by.lower() if sort_by and sort_type and sort_type.lower()=='desc' else sort_by.lower() 
        print("item",item_name)
        print("sort",sort_by)
        category_data=Item.objects.filter(
            item_name
            ).order_by(sort_by)[pagination['offset']:pagination['offset'] + pagination['limit']]

        print("query",str(category_data.query))
        # category_data=Item.objects.raw("""select * from store_item where status_id != '3'{search} 
        #                                         limit {offset},{limit};""".format(
        #                                             search=search,offset=pagination["offset"],limit=pagination["limit"]
        #                                         ))
        print(category_data)
        serialized_data=ItemSerializer(category_data,many=True)
        print(serialized_data.data)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
        
    def put(self,request):
        try:
            item_data=Item.objects.get(Q(id=self.request.data["id"]),~Q(status_id=3))
            print(item_data)
            serialized_data=ItemSerializer(item_data,data=self.request.data,partial=True)
            serialized_data.is_valid()
            serialized_data.save()
            #print(serialized_data.errors)
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({"message":"Item not exist!."},status=status.HTTP_200_OK)
        except:
            return Response({"errors":"Can't update!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request):
        print(self.request)
        try:
            item_data=Item.objects.get(Q(id=self.request.data["id"]),~Q(status_id=3))
            item_data.status_id=3
            item_data.save()
            return Response({"message":"Successfully removed."},status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({"message":"Item not exist!."})
        except:
            return Response({"error":"Can't remove!."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
# Add Rack
class CRUDRack(APIView):

    def get(self,request):
        sort_by=self.request.GET.get("sort_by")
        sort_type=self.request.GET.get("sort_type")
        per_page_rows=self.request.GET.get("per_page")
        page_no=self.request.GET.get("page_no")
        id=self.request.GET.get("id")
        search=''
        if id:
            search+=' and id={}'.format(id)
        if sort_by:
            search+=' order by {}'.format(sort_by)
        if not sort_by:
            search+=' order by id'
        if sort_type:
            search+=' {}'.format(sort_type)
        print("ff",page_no,per_page_rows)
        if per_page_rows:
            per_page_rows=int(per_page_rows)
        if page_no:
            page_no=int(page_no)
        if not per_page_rows:
            per_page_rows=None
        if not page_no:
            page_no=None
        print(page_no,per_page_rows)
        pagination=get_pagination(per_page_rows=per_page_rows,page_no=page_no)
        print(pagination)
        rack_data=Rack.objects.raw("""select * from store_rack where status_id != '3'{search} 
                                                limit {offset},{limit};""".format(
                                                    search=search,offset=pagination["offset"],limit=pagination["limit"]
                                                ))
        print(rack_data)
        serialized_data=RackSerializer(rack_data,many=True)
        print(serialized_data.data)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        print(type(self.request.data))
        serialized_data=RackSerializer(data=self.request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response({"errors":serialized_data.errors},status=status.HTTP_200_OK)

    def put(self,request):
        try:
            rack_instance=Rack.objects.get(id=self.request.data.pop("id"))
            print(self.request.data)
            serialized_data=RackSerializer(rack_instance,self.request.data)
            if serialized_data.is_valid():
                return Response(serialized_data.data,status=status.HTTP_200_OK)
            return Response({"errors":serialized_data.errors},status=status.HTTP_200_OK)
        except Rack.DoesNotExist:
            return Response({"message":"Pleaase enter valid rack!."},status=status.HTTP_200_OK)
        except:
            return Response({"errors":"Can't update!."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request):
        try:
            rack_data=Rack.objects.get(id=self.request.data["id"])
            rack_data.status_id=3
            rack_data.save()
            return Response({"message":"Removed successfully."},status=status.HTTP_204_NO_CONTENT)
        except Rack.DoesNotExist:
            return Response({"message":"Rack Does not exist!."},status=status.HTTP_200_OK)
        except:
            return Response({"errors":"Can't remove!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)