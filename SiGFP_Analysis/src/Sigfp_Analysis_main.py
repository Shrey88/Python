from FetchAnalysisData import FetchAnalysisData
from GraphCreation import GraphCreation
from WorkBook import WorkBook


def main():
    afc = FetchAnalysisData()
    wb = WorkBook(data=afc.fetch_data(), column_header=afc.get_column_header(),
                  output_file="..\\_output\\SiGFP_Summary_Report.xlsx")
    wb.write_data()
    wb.wb_object.close()

    open_wb = WorkBook(filename="..\\_output\\SiGFP_Summary_Report.xlsx")

    graphc = GraphCreation(open_wb.active_sheet)
    open_wb.active_sheet.add_chart(graphc.create_graph(), "I4")
    open_wb.wb_object.save("..\\_output\\SiGFP_Summary_Report_1.xlsx")
    open_wb.wb_object.close()


if __name__ == '__main__':
    main()
