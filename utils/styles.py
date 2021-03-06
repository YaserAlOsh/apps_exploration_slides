#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IPython.core.display import display, HTML
display(HTML("""<style>

@font-face {
    font-family: 'Cooper Hewit' ;
    src: url(utils/CooperHewitt-Medium.otf);
}

@font-face {
    font-family: 'Cooper Hewit Bold' ;
    src: url(utils/CooperHewitt-Bold.otf);
}

@font-face {
    font-family: 'Cooper Hewit Light' ;
    src: url(utils/CooperHewitt-Light.otf);
}

.container {
    width:96% !important;
    font-family: 'Cooper Hewit','Source Sans Pro', 'Open Sans', 'Helvetica', Sans;
}

.text_cell_render h1 {
    text-align: center;
    font-family: 'Cooper Hewit Light';
    font-size: 52px;
}

strong {
    font-weight: bold;
}

h2, h3 {
    font-family: 'Cooper Hewit Bold' ;
}

.text_cell_render p,
.text_cell_render h2,
.text_cell_render h3,
.text_cell_render h4,
.text_cell_render ul,
.text_cell_render ol,
.text_cell_render pre,
.text_cell_render table {
    max-width: 860px;
    margin: 0 auto;
    line-height: 30px;
}

.text_cell_render p,
.text_cell_render ul,
.text_cell_render ol,
.text_cell_render table {
    font-family: 'Cooper Hewit' ;
    font-size: 20px;
    padding-bottom : 26px;
}

.text_cell_render h4 {
    font-size: 20px;
    text-align: center;
}

.text_cell.rendered .input_prompt {
    display : none !important;
}

.text_cell_render table {
    width: 860px;
    margin: 26px auto;
    text-align: center;
}

.text_cell_render td,
.text_cell_render th {
    padding: 8px;
    text-align: center;
}

.text_cell_render table thead {
    background-color: #333;
    color: white;
    font-family: 'Cooper Hewit Light';
    text-align: center;
}

.CodeMirror {
    padding: 8px 20px;
}
.CodeMirror pre {
    font-size: 20px;
    line-height: 28px;
}

div.output_text pre {
    color: #333;
    font-size: 18px;
    line-height: 26px;
}
.output_png img{
    margin: 0 auto;
    margin-top: 12px;
    display: block;
    min-width: 600px;
}

.rendered_html blockquote cite:before {
    content: '— ';
}
.rendered_html blockquote p:before {
    content: "“";
    font-size: 160px;
    color: rgba(218, 218, 218, 0.68);
    position: relative;
    margin-left: -72px;
    top: 32px;
    left: 37px;
    font-family: Cooper Hewitt Bold;
    z-index: 0;
}
.rendered_html blockquote {
    clear: both;
    border: none;
}

.rendered_html blockquote p:after {
    visibility: hidden;
    display: block;
    content: "";
    clear: both;
    height: 0;

}

.rendered_html blockquote cite {
    display: block;
    padding-left: 30%;
    padding-right: 10%;
    text-align: right;
    margin-top: 12px;
}

li > * > li {
    margin-left: 24px;
    line-height: 30px;
}

.rendered_html li {
    padding-bottom: 12px;
    padding-left: 12px;
    margin-left: 20px;
}

li > ul,
li > ol {
    margin-top: 12px !important;
    padding-bottom: 0px !important;
}

.rendered_html strong {
    font-family: 'Cooper Hewit Bold';
    color: #007eff;
}

</style>"""))
