<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="#all">
    
    <xsl:output method="xml"/>

    <xsl:template match="text()">
        <xsl:value-of select="."/>
    </xsl:template>
    
    <xsl:template match="tei:teiHeader">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="tei:div">
        <!-- "div case" trace -->
        <div>
            <xsl:apply-templates select="node()"/>
        </div>
    </xsl:template>
    
    <xsl:template match="tei:p">
        <p>
            <xsl:attribute name="facs">
                <xsl:value-of select="@facs"/>
            </xsl:attribute>
            <xsl:apply-templates select="node()"/>
        </p>
    </xsl:template>
    
    <xsl:template match="tei:l">
        <xsl:apply-templates select="node() normalise-space($text)"/>
    </xsl:template>
    
    <xsl:template match="tei:quote">
        <xsl:apply-templates select="node()"/>
    </xsl:template>
    
    <xsl:template match="tei:choice">
        <xsl:apply-templates select="tei:sic/text()"/>
        <xsl:if test="not(following-sibling::tei:corr)">
            <xsl:text> (</xsl:text><xsl:apply-templates select="tei:corr/text()"/><xsl:text>)</xsl:text>
        </xsl:if>
    </xsl:template>
    
    <xsl:template match="tei:rs">
        <xsl:apply-templates select="tei:rs/node()"/>
    </xsl:template>
    
    <xsl:template match="tei:add">
        <sup>
            <xsl:apply-templates select="node()"/>
        </sup>
    </xsl:template>
    
    <xsl:template match="tei:del">
        <s>
            <xsl:apply-templates select="node()"/>
        </s>
    </xsl:template>
    
    <xsl:template match="*">
        <xsl:copy>
            <xsl:apply-templates select="node()"/>
        </xsl:copy>
    </xsl:template>
    
</xsl:stylesheet>
