def lambda_handler(event, context):
    emoji_type = event["emoji_type"]
    message = event["message"]
    
    feeling = None
    
    if emoji_type == 0:
        feeling = "positive"
    elif emoji_type == 1:
        feeling = "neutral"
    else:
        feeling = "negative"
        
    response = {
        "feeling": feeling,
        "message": message,
    }
    
    return response
