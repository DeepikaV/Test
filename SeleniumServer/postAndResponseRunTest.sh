while (! test -e /Users/Shared/Jenkins/Home/jobs/postAndResponse/workspace/Output/report.html)
do
    echo "Waiting report.html ..."
    sleep 10
done
echo "Found report.html ... Proceed to kill all Terminals"
osascript -e 'tell app "Terminal" to quit'