import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
name_pattern = r'(?:title-link">)([^<]+)'
location_pattern = r'(?:location">\n+\s+)([^\n]+)'
number_pattern = r'(?:Телефон.+\s+<dd class="spec__value">)([^<]+)'
time_pattern = r'(?:Часы работы.+\s+<dd class="spec__value">)([^<]+)'
response = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()
# print(response)

match_name = re.findall(name_pattern, response)
match_location = re.findall(location_pattern, response)
match_number = re.findall(number_pattern, response)
match_time = re.findall(time_pattern, response)
result_list = []
for i in range(len(match_name)-1):
    result_list.append([match_name[i],  match_location[i], match_number[i], match_time[i]])
    print([match_name[i],  match_location[i], match_number[i], match_time[i]])

# print(f"{result_list}")