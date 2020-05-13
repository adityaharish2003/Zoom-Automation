#parse content of word timetable 
from docx import Document
from csv import reader , writer
def wordParse(passDoc):
    wordDoc = Document(passDoc)
    t = wordDoc.tables[0]
    wordContent = []
    for row in t.rows:
        for cell in row.cells:
            wordContent.append(cell.text.strip())
    wordContent = wordContent[5:]
    with open('pass.csv') as csv_handle:
        csv_content = list(reader(csv_handle))
    for i in range(3 ,len(wordContent) , 5):
        for j in range(len(csv_content)):
            if wordContent[i] == csv_content[j][0]:
                if wordContent[i+1] != csv_content[j][1] :
                    csv_content[j][1] = wordContent[i+1].strip()  
    with open('pass.csv' , 'w' , newline='') as csvWriteHandle:
        csvWriter = writer(csvWriteHandle)
        csvWriter.writerows(csv_content)
    with open('pass.csv') as csv_handle:
        csv_content = list(reader(csv_handle))
