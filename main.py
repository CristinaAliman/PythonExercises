posts = [
    {
        "name": "post1",
        "impressions": 345000, 
        "link_clicks": 34
    },
    {
        "name": "post2",
        "impressions": 546000, 
        "link_clicks": 123
    },
    {
        "name": "post3",
        "impressions": 387000, 
        "link_clicks": 345
    }
]

posts_two = [
    {
        "name": "post1",
        "impressions": 12000, 
        # "link_clicks": 34
    },
    {
        "name": "post2",
        "impressions": 12000, 
        # "link_clicks": 123
    },
    {
        "name": "post3",
        "impressions": 12000, 
        # "link_clicks": 345
    }
]

def post_ctr(post_list):
    ctrs = []
    for post in post_list:
        if "link_clicks" not in post:
            return ctrs
        if "impressions" not in post:
            return ctrs    
        
    for post in post_list:
        clicks = post['link_clicks']
        impressions = post['impressions']
        ctr = clicks / impressions * 100
        ctrs.append(round(ctr,2))
    return ctrs


def avg_p_ctr(ctr_list):
    total = 0
    count = 0
    for ctr in ctr_list:
        total = total + ctr
        count = count + 1
    if count == 0:
        return 0

    average = total / count
    return average

# Running things here
ctr_list = post_ctr(posts_two)
print("ctr_list", ctr_list)

avg = avg_p_ctr(ctr_list)
print("final", avg)


# print( avg_p_ctr( post_ctr( posts_two ) ) )