#(C)Tsubasa Kato 2020/11/7
#Last Updated on 2020/12/29
#Random Number Generator 
$counter = 1;
@number = 0;
$limit = 10000;
#decide upper limit of how many random numbers generated:
while ($counter <= $limit){
	$random_number = int(rand(10));
	@number[$counter] = $random_number;
	print "$counter: $random_number\n";
	$counter = $counter+1;

	$both = $both.@number[$counter - 1];
	
	
}

#prints all numbers made randomly.
print $both;
print @number[$counter];
#code used from: https://stackoverflow.com/questions/12948136/digit-occurence-of-a-number-in-perl
my (%counts, $sum);

while ($both =~ m/(\d)/g) {

    $counts{$1}++;
    $sum++;
}

print "The count each digit appears are: \n";
print "'$_' - $counts{$_}\n" for sort keys %counts;
print "The sum of all the totals is $sum\n";
