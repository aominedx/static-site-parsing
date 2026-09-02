
import xlsxwriter
from parse_killprice import parse


def download_excel(param):
    book = xlsxwriter.Workbook('D:\\PythonProject24\\killprice.XLSX') #создать эксель и выбрать расположение
    page = book.add_worksheet('товар')

    row = 0
    col = 0

    page.set_column("A:A",20)
    page.set_column("B:B",20)
    page.set_column("C:C",200)
    page.set_column("D:D",70)

    for item in param():

        page.write(row,col,item[0])
        page.write(row,col+1,item[1])
        page.write(row,col+2,item[2])
        page.write(row,col+3,item[3])

        row+=1
    book.close()

download_excel(parse)
