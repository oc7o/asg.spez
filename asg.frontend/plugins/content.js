var QuillDeltaToHtmlConverter =
  require('quill-delta-to-html').QuillDeltaToHtmlConverter

export default ({ app }, inject) => {
    inject('content', content => {
        var deltaOps = [
            ...content.ops
        ]
    
        var cfg = {}
    
        var converter = new QuillDeltaToHtmlConverter(deltaOps, cfg)
    
        var html = converter.convert().replace("<h1>", '<h1 class="title">').replace("<h2>", '<h2 class="subtitle">')
        return html
    })
}