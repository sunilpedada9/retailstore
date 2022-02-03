# Pagination
def get_pagination(**kwarg):
    if (kwarg['page_no']==0) or (kwarg['page_no'] is None):
        limit_offset={'limit':kwarg['per_page_rows'],'offset':0}
        if (kwarg['per_page_rows']==0 or kwarg['per_page_rows'] is None):
            limit_offset['limit']=5
        return limit_offset
    else:
        offset=(kwarg['page_no']-1)* kwarg['per_page_rows']
        return {'limit':kwarg['per_page_rows'],'offset':offset}

def get_paginaation_data(*kwarg):
    total_items=kwarg['count']
    total_pages=int(kwarg['count']/kwarg['limit'])
    if kwarg['page_no']==0:
        current_page=1
    else:
        current_page=kwarg['page_no']
    return {'total_pages':total_pages,'current_page':current_page,'total_items':total_items}

def jwt_response_payload_handler(token,user=None,request=None):
    return{
        'token':token,
        'user_name':user.username
    }