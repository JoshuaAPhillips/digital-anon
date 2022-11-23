<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns="http://www.w3.org/1999/xhtml"
    version="2.0">
    
    <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
    <link rel="stylesheet" type="text/css" href="../resources/style.css"/>
    <script type="text/js" src="../resources/modal.js"/>
    
    <!-- master template -->
    
    <xsl:template match="/">
        <xsl:result-document href="../html/{tei:TEI/@xml:id}.html">
            <xsl:element name="html">
                <xsl:element name="head">
                    <xsl:element name="title">
                        <xsl:value-of select="//tei:titleStmt/tei:title"/>
                    </xsl:element>
                </xsl:element>
                    <xsl:element name="body">  
                        <xsl:apply-templates select="child::node()"/>
                    </xsl:element>
            </xsl:element>
        </xsl:result-document>
    </xsl:template>
    
    <!-- title h1 -->
    
    <xsl:template match="//tei:titleStmt/tei:title">
        <xsl:element name="h1">
            <xsl:value-of select="//tei:titleStmt/tei:title"/>
        </xsl:element>
    </xsl:template>
    
    <!-- author h2 -->
    
    <xsl:template match="tei:titleStmt/tei:author">
        <xsl:element name="h2">
            <xsl:value-of select="//tei:titleStmt/tei:author"/>
        </xsl:element>
    </xsl:template>
    
    <!-- page ref h3s -->
    
    <xsl:template match="//tei:div">
        <xsl:element name="h3">
            <xsl:text>Page: </xsl:text><xsl:value-of select="@xml:id"/>
        </xsl:element>
        <xsl:apply-templates/>
    </xsl:template>
    
    <!-- body text -->
    
    <xsl:template match="//tei:body/tei:div/tei:p">
        <xsl:element name="br"/>
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="tei:l">
        <xsl:element name="p">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <!-- choice tags -->

    <xsl:template match="//tei:choice/tei:corr">
        <xsl:element name="span">
            <xsl:attribute name="class">
                <xsl:text>corr</xsl:text>
            </xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="//tei:choice/tei:sic">
        <xsl:element name="title">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <!-- del tags --> 
    
    <xsl:template match="//tei:p/tei:l/tei:del">
        <xsl:element name="span">
            <xsl:attribute name="class">
                <xsl:text>del</xsl:text>
            </xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <!-- add tags -->
    
    <xsl:template match="//tei:l/tei:add">
        <xsl:if test="@place='above'">
            <xsl:element name="span">
                <xsl:attribute name="class">
                    <xsl:text>add-above</xsl:text>
                </xsl:attribute>
                <xsl:apply-templates/>
            </xsl:element>
        </xsl:if>
        
        <xsl:if test="@place='inline'">
            <xsl:element name="span">
                <xsl:attribute name="class">
                    <xsl:text>add-inline</xsl:text>
                </xsl:attribute>
                <xsl:apply-templates/>
            </xsl:element>
        </xsl:if>

        
    </xsl:template>
    
    <!-- rs -->
    
    <xsl:template match="//tei:l/tei:rs">
        <xsl:element name="a">
            <xsl:attribute name="href">
                <xsl:value-of select="[@ref]"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
</xsl:stylesheet>