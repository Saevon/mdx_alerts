What is it
==========

A Python Markdown extension that allows you to add twitter-bootstrap based alerts.

    See: http://getbootstrap.com/components/#alerts


# Installation

    $ pip install git+git://github.com/Saevon/markdown-alerts.git

# Usage

Activate the `alerts` extension and use the following markup:

```html
!alert! info
Wow! this extension works.
!endalert!
```

This will give you an alert with a success icon, and the given text.

Check [Twitter Bootstrap](http://getbootstrap.com/components/#alerts) for their alert levels. This plugin makes `error` an alias for `danger` since I feel it is a more intuitive title for that alert level.

You can embed other markup inside the alert, though the result might get a bit crowded.

### Icon

To get rid of the icon, or specify your own try the following:

```html
!alert! warning noicon
    <strong>Noo!</strong>, no icon here!
!endalert!
```

```html
!alert! success unlock-alt
     <strong>Dang!</strong>, we changed the icon so easily!
!endalert!
```

### Dismissable Alerts

You can also get them to have an `x` so that they can be dismissed, just do the following:

```html
!alert! error dismissable
     Don't make me go away! Though you can...
!endalert
```

Watch out! If you want both a custom/no icon then you need to put them in the right order

```html
!alert! level dismissable noicon
    Data!
!endalert!
```


### Indentation

For the markdown to be readable as txt indentation is supported. Any indentation that is 4 spaces or more those first 4 spaces.



# Troubleshooting

Please consider using [Github issues tracker](http://github.com/Saevon/markdown-alerts/issues) to submit bug reports or feature requests.


# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
