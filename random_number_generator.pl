#(C)Tsubasa Kato 2020/11/7
#Random Number Generator 
$counter = 0;
@number = 0;
#decide upper limit of random numbers generated here (10000 in this case)
while ($counter <= 10000){
	@number[$counter] = $random_number;
	$random_number = int(rand(10));	
	print "$counter: $random_number\n";
	$counter = $counter+1;

	if ($counter > 0){
		$both = $both.@number[$counter - 1];
	}
	
}
#prints all numbers made randomly.
print $both;
#code used from: https://stackoverflow.com/questions/12948136/digit-occurence-of-a-number-in-perl
my (%counts, $sum);

while ($both =~ m/(\d)/g) {

    $counts{$1}++;
    $sum++;
}

print "The count each digit appears is: \n";
print "'$_' - $counts{$_}\n" for sort keys %counts;
print "The sum of all the totals is $sum\n";



