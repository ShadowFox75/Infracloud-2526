APIKEY="cisco|orlanqAUbbCNrlFzfSujm5BDdOeAs6M5h-EJ4FcKhg8"
for BOOK in {900..999}
do 
 echo $BOOK
 DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
 echo $DELETE_URL
 curl -X DELETE $DELETE_URL -H "accept: application/json" -H "X-API-KEY:$APIKEY" -H "Content-Type: application/json"
done
