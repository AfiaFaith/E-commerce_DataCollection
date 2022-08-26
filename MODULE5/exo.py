from libraries.utils import Utils
from libraries.datacsv import CsvFactory
from libraries.datajson import JsonFactory
from libraries.datahtml2 import HtmlFactory
from libraries.factories import concatenateList


if __name__ == '__main__':
    print(Utils.divider())
    print('\n')
    print(CsvFactory.main())
    print('\n')
    print(JsonFactory.main())
    print('\n')
    print(HtmlFactory.main())
    print('\n')
    print(concatenateList.concatenate(HtmlFactory.main(), CsvFactory.main(), JsonFactory.main() ))