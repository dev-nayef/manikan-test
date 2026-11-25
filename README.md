# تنسيقك | Outfit Builder

A lightweight Arabic-first storefront demo for composing a clothing outfit from original product images.

## Features

- Choose one shirt, one pair of pants, and one pair of shoes.
- Preview the selected pieces in an outfit layout: shirt above pants, shoes below.
- Pure black preview background.
- Compose the preview directly in the browser with the Canvas API.
- Download the final composition as a PNG.
- Add store products from the browser using the product management panel.
- No customer photo upload, human body, face, or mannequin.
- No AI image generation and no external API required.

## Run

Open [index.html](./index.html) in a modern browser, or enable GitHub Pages:

1. Open the repository **Settings**.
2. Select **Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the `main` branch and `/ (root)`, then save.

The site is static and can be hosted on GitHub Pages.

## Add your store products

Use **إدارة المنتجات · إضافة قطعة جديدة** in the page. Upload a product image and choose its category.

For the cleanest result, upload a transparent PNG or WebP image with the product already isolated from its background. The browser stores added products in local storage on that device only. This first version does not include a shared database or an admin login, so products added in one browser are not automatically visible to other customers.

## Project structure

- `index.html` — complete responsive interface, demo catalog, product selection, Canvas composition, local product management, and PNG export.

## Notes

This is an initial front-end prototype. It uses illustrative demo product images. Replace them with the store's real transparent product photos before publishing to customers.
