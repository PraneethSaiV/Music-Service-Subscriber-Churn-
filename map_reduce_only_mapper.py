from mrjob.job import MRJob
from operator import add

class GetAggregate(MRJob):
    def mapper(self, _, line):
        (index,msno,date,twenty5,fifty,sevenT5,nineT8,hundered,unique,Total) = line.split(',')
        if date[:6] > '201607':
            yield (msno, date[:6]), (twenty5,fifty,sevenT5,nineT8,hundered,unique,Total)
    def reducer(self, key, value_list): 
        final_list = [0,0,0,0,0,0,0]
        for sub_list in value_list:
            try:
                final_list = map(add, [float(x) for x in sub_list], [float(y) for y in final_list])
            except:
                continue
        yield key, final_list
if __name__ == '__main__':
    GetAggregate.run()
        
    
