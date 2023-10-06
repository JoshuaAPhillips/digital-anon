xquery version "3.1";

import module namespace xmldb="http://exist-db.org/xquery/xmldb";

declare namespace tei="http://www.tei-c.org/ns/1.0";

declare variable $collection := collection("/db/transcriptions");

declare function local:simplifier($file as node()*)
  {
    let $modified_file :=
      typeswitch ($file)
        case text() return 
          $file
        case element(tei:teiHeader) return
          ()
        case element(tei:div) return
          <div>{ local:simplifier($file/node()) }</div>
        case element(tei:p) return
          <p>{ local:simplifier($file/node()) }</p>
        case element(tei:l) return
          (
            local:simplifier($file/node()),
            if (not($file/following-sibling::tei:l)) then () else <br/>
          )
        case element(tei:choice) return
          (
            local:simplifier($file/tei:corr),
          if (not($file/following-sibling::tei:sic)) then () else <span> { local:simplifier($file/tei:sic) } </span>
          )
        case element(tei:add) return
          <sup>{ local:simplifier($file/node()) }</sup>
        case element(tei:del) return
          <s>{ local:simplifier($file/node()) }</s>
      default return
        $file

    return $modified_file
  };

for $file in $collection return
  let $filename := string-join("simplified_" || $file//tei:idno)
  return xmldb:store("/db/transcriptions/simplified/", $filename, local:simplifier($file))