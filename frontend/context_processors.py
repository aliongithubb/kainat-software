from urllib import request

def global_variables(request):
    # Define the variables for all views
    title = 'Kainat Plastic Industry'
    
    data = {
        'title': title,
    }

    # Return a dictionary containing the variable
    return data