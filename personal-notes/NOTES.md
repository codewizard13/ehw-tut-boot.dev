<link rel="stylesheet" href="../css/notes.css" />

# TUTORIAL NOTES:

<a class="bookmark-link" href="#bookmark">JUMP TO BOOKMARK</a>

| **Tutorial Name**    | **Custom Elementor Widget: Simple Example**               |
| -------------------- | --------------------------------------------------------- |
| File Name            | NOTES.md                                                 |
| Date Created         | 12/28/23                                                  |
| Date Modified        | --                                                        |
| Platform             | Website                                                   |
| Channel              | [Elementor Developers](https://developers.elementor.com/) |
| Version              | 0.0.1                                                     |
| Programmer / Student | **Eric Hepperle**                                         |

* **Tutorial URL:** https://developers.elementor.com/docs/widgets/simple-example/

---

### Folder Structure

```bash
elementor-oembed-widget/
|
├─ widgets/
|  └─ oembed-widget.php
|
└─ elementor-oembed-widget.php
```

### LOCATIONS

- **REPO FOLDER:** ehw-tutwrk-ele-oembed-widget
- **URL:** http://lardev-elsms.test/
- **Folder:** T:\Laragon\lardev-elsms\wp-content\plugins\ehw-tutwrk-ele-oembed-widget
- **WEB SERVER:** Laragon
- **GITHUB:** https://github.com/codewizard13/ehw-tutwrk-ele-oembed-widget


- Set `WP_DEBUG` to **true** in **wp-config.php**: This ensures that any errors will be displayed on screen.

#### #TIP: In the past we would have recommended to set WP_DEBUG back to false in production environments. However, this set of code leaves debugging enabled, logs it to a file, and doesn't display in views -- so no user sees the error messages unless they go and view the error.log file.

```php
// Enable WP_DEBUG mode
define( 'WP_DEBUG', true );

// Enable Debug logging to the /wp-content/debug.log file
define( 'WP_DEBUG_LOG', true );

// Disable display of errors and warnings
define( 'WP_DEBUG_DISPLAY', false );
@ini_set( 'display_errors', 0 ); // WPE auto-added this setting
```

---

- Navigate to `wp-content/plugins` folder
- Create new plugin folder - the folder name will be same as your main PHP file: `ehw-tutwrk-ele-oembed-widget/`
- Create new addons main controller file: `ehw-tutwrk-ele-oembed-widget.php` inside plugin folder
- Create file: `oembed-widget.php` in widgets/


<span class="code-filename"> ehw-tutwrk-ele-oembed-widget.php</span>


- Create comment block as follows:

```php
/**
 * Plugin Name: Elementor oEmbed Widget
 * Description: Auto embed any embbedable content from external URLs into Elementor.
 * Plugin URI:  https://elementor.com/
 * Version:     1.0.0
 * Author:      Elementor Developer
 * Author URI:  https://developers.elementor.com/
 * Text Domain: elementor-oembed-widget
 *
 * Elementor tested up to: 3.16.0
 * Elementor Pro tested up to: 3.16.0
 */
```


<span class="code-filename">oembed-widget.php</span>


---


## BOOKMARK