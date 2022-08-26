from librairies.utils import Utils
from librairies.datacsv import CsvFactory
from librairies.datajson import JsonFactory
from librairies.datahtml import HtmlFactory
from librairies.concatmethode import concatenateList


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