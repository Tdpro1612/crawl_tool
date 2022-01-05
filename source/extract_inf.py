


# hàm tách ra xpath

def track_xpath(xpath):
    if 'xpath' in xpath:
        track_xpath=xpath.split('_')
        return track_xpath
    
# hàm lưu column    
def create_columns(data):
    columns=[]
    for i in data:
        #print(i)
        for key in i.keys():
            #print(key)
            result=track_xpath(key)
            if result != None and 'click' not in result:
                #print(result)
                columns.append(result[1])
    return columns