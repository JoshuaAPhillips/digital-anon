xquery version "3.1";

declare namespace tei="http://www.tei-c.org/ns/1.0";

let $collection := collection("/db/transcriptions")

for $file in $collection
return $file//tei:idno/child::text()