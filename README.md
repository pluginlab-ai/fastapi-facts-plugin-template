# FastAPI Facts Plugin Template

![template-img](https://firebasestorage.googleapis.com/v0/b/pluginlab.appspot.com/o/public%2Ftemplates%2Ffastpi-template.jpg?alt=media)

This starter ChatGPT Plugin template allows you to use FastAPI on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

To use it, you only have to follow the steps on [PluginLab](https://pluginlab.ai).
[PluginLab](https://pluginlab.ai) will let you configure and manage your plugin OAS and manifest files.

The other advantage of using [PluginLab](https://pluginlab.ai) is that you will be able to configure OAuth and Monetization for your ChatGPT plugin in 5 minutes.

## How it works

* Go to [PluginLab](https://pluginlab.ai).
* Click on "Create Plugin" and select this template.
* Follow the deployment steps.
* Enjoy your plugin!

## Running Locally using Vercel

```bash
npm i -g vercel
vercel dev
```

Your FastAPI api is now available at `http://localhost:3000`.

## Running Locally using Docker

```bash
docker build -t <image_name> .
docker run -p 3000:8000 <image_name>
```

Your FastAPI api is now available at `http://localhost:3000`.

## Adding Authentication

You can add authentication to this plugin in a few clicks by using [PluginLab](https://pluginlab.ai).
Please check our [documentation](https://docs.pluginlab.ai/en/category/authentication-nyfktk/) about authenticating users.

## Adding Monetization

You can add monetization to this plugin in a few clicks by using [PluginLab](https://pluginlab.ai).
Please check our [documentation](https://docs.pluginlab.ai/en/category/plugin-monetization-10nw5z4/) about monetizing your plugin.

