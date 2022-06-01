import pandas as pd
data = pd.read_csv("SimilarityAndOtherInfo_500_Copy.csv",keep_default_na=False)

Reviewer_ID = data['Reviewer ID'].tolist()
Name = data["Name"].tolist()
Paper_ID = data["Paper ID"].tolist()
Confidence = data["Confidence"].tolist()
Cosine_Similarity = data["Cosine Similarity"].tolist()
Jaccard_Similarity = data ["Jaccard Similarity"].tolist()

unique_confidence_value= list(set(Confidence))
temp_dict = {}
for i in range(0,len(unique_confidence_value)):
   temp_dict[unique_confidence_value[i]] = Confidence.count(unique_confidence_value[i])
print(temp_dict)

point_loop = []
for i in range(1,6):
   point_loop.append(i/10)

print(point_loop)
temp_dict2 = {}
for x in point_loop:
   temp_list = []
   for y in Cosine_Similarity:
      if str(x) in str(y):
         temp_list.append(y)
   temp_dict2[x]=temp_list

print(temp_dict2)


