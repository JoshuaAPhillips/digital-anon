xquery version "3.1";

declare namespace tei="http://www.tei-c.org/ns/1.0";

declare variable $collection := collection("/db/transcriptions");

let $filename := "network-test-3.tsv"

let $allPersons := $collection//tei:div//tei:rs/@key

let $countI := count($allPersons[.= $allPersons])
let $countJ := count($allPersons[.= $allPersons])

let $content := string-join(
  for $div in $collection//tei:div
  let $persons := $div//tei:rs/@key
  where count($persons) > 1
  for $i in $persons
  let $countP := count($div//*[tei:rs/@key = $i and $i = tei:rs/@key])
  for $j in $persons
  where $i != $j and $countP > 0
  return concat($i, "&#x9;", $countI, "&#x9;", $j, "&#x9;", $countJ, "&#x9;", $countP, codepoints-to-string(xs:integer(10)))
, "")

let $doc-db-uri := ("/db", $filename, $content, "text/plain")
return $doc-db-uri