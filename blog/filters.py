from blog import app
import mistune

@app.template_filter()
def dateformat(date, format):
    if not date:
        return None
    return date.strftime(format)
  
@app.template_filter()
def markdown(content):
  if not content:
    return None
  content = mistune.markdown(content)
