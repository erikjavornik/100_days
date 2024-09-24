Three methods to add CSS to HTML:
- Inline:`<tag style="css" />`
    
    `<html style="background:blue"></html>`
    - Good for adding to a single element on the page. Not practical if style is shared between multiple elements.
- Internal: `<style>css</style>`
    ````html 
    <html>
        <head>
            <style>
                html{
                    background:red;
                }
            </style>
        </head>
    </html>
    ````
    - Not useful if there are multiple pages
- External: `<link href="style.css"/>`
    ````html 
    <html>
        <head>
            <link
                rel="stylesheet"
                href="./styles.css"
            />
        </head>
    </html>
    ````
    ````css
    html{
    background:red;
    } 
    ````