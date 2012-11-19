while (! test -e /Users/Shared/Jenkins/Home/jobs/dealsAndBuyNowTabVisible/workspace/Output/report.html)
do
    echo "Waiting report.html ..."
    sleep 10
done
echo "Found report.html ... Proceed to kill all Terminals"
osascript -e 'tell app "Terminal" to quit'