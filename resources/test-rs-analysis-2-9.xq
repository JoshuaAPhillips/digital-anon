xquery version "3.1";

declare namespace tei="http://www.tei-c.org/ns/1.0";

declare variable $collection := collection("/db/transcriptions");

let $filename := "digital-anon-names-test-3.tsv"
let $content := string-join(
  for $div in $collection//tei:div
  let $persons := $div//tei:rs[@type="person"]
  where count($persons) > 1
  for $i in $persons
  for $j in $persons
  let $countP := count($div//*[tei:rs[@type="person"] = $i and tei:rs[@type="person"] = $j])
  where $i != $j and $countP > 0
  return concat($i, "&#x9;", $countP, "&#x9;", $j, codepoints-to-string(xs:integer(10)))
, "")

let $doc-db-uri := xmldb:store("/db/output", $filename, $content, "text/plain")
return $doc-db-uri