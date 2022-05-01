# Google Cloud

Первой мыслью были [Github Pages](https://docs.github.com/en/pages), но сервис поддерживает только статические страницы, причем к одному аккаунту можно привязать только один сайт.[^gh-pages-single-site]

[^gh-pages-single-site]: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites

Изначально рассматривал Hiroku (узнал из[статьи](https://blog.patricktriest.com/host-webapps-free/)), но компания временно приостановила создание аккаунтов из РФ.

Google выбрал после беглого просмотра доков - понятные и подробные. К тому же, есть много бесплатных продуктов [^google-free]. Для хостинга веб-приложений рекомендует[^google-cloud-chooce] [Cloud Run](https://cloud.google.com/run).

[^google-free]: https://cloud.google.com/free/
[^google-cloud-chooce]: https://cloud.google.com/hosting-options

## Free Tier

В первую очередь, меня интересовал вопрос: "Сколько web-приложений можно "втиснуть" в рамки бесплатных[^google-free-tier] ежемесячных лимитов?"

[^google-free-tier]: см. раздел Free Tier
    https://cloud.google.com/free/docs/gcp-free-tier

1 приложение - 1 проект. Бесплатно можно до 30 [проектов](https://cloud.google.com/resource-manager/docs/creating-managing-projects) внутри одного [billing аккаунта](https://cloud.google.com/billing/docs/how-to/manage-billing-account), а их суммарное потребление ресурсов не должно превышать месячный лимит.

> The free tier usage is aggregated across projects by billing account and resets every month; you are billed only for usage past the free tier. The free tier is applied as a spending based discount using Tier 1 pricing. [^google-cloud-pricing]

[^google-cloud-pricing]: см. начало раздела Pricing tables
    https://cloud.google.com/run/pricing

При регистрации аккаунта на Google Cloud активируется 12-месячный Trial с $300 для экспериментов. Можно не дожидаться окончания триала и сделать аккаунт billing (подключить дебетовую карту). Бонусные $ с триала остаются[^trial-to-billing].

[^trial-to-billing]: уточнить в офф. доках или FAQ
    информация отсюда https://www.appsadmins.com/blog/complete-guide-to-free-google-service
    возможно где-то здесь https://support.google.com/cloud/answer/6330231

Лимиты следующие: [^cloud-run-free-tier-limits]
- 2 million requests per month
- 360,000 GB-seconds of memory, 180,000 vCPU-seconds of compute time
- 1 GB network egress from North America per month

[^cloud-run-free-tier-limits]: https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits

Прежде всего здесь нужно понимать, что каждое приложение запускается в "облаке", как контейнер. Что это значит?

Далее можно попробовать разобраться с тем, как именно отдельное приложение (контейнер) расходуется ресурсы. Возможно, помогут разделы документации:
- [Resource model](https://cloud.google.com/run/docs/resource-model);
- [Concurrency](https://cloud.google.com/run/docs/about-concurrency); 
- [Cloud Run Quotas and Limits](https://cloud.google.com/run/quotas) 

# Ссылки на материалы для старта

[Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

[Deploy a Python service to Cloud Run (GC console in browser)](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)

[Installing the gcloud CLI (офф. доки)](https://cloud.google.com/sdk/docs/install#linux)

[Setting Up Google Cloud SDK For GCP On Arch/Manjaro Linux](https://dev.to/nabbisen/setting-up-google-cloud-sdk-of-gcp-on-archmanjaro-linux-19mk)

[Setting Up Your Environment (офф. доки)](https://cloud.google.com/run/docs/setup)

[Деплой через gcloud cli из исходников](https://cloud.google.com/run/docs/deploying-source-code)

[Deploy a container to Cloud Run](https://cloud.google.com/run/docs/quickstarts/deploy-container)


# Прочие материалы

[Большое FAQ на Github по Google Cloud](https://github.com/ahmetb/cloud-run-faq)

[Статья-гайд по хостингку веб-приложений на Google Cloud](https://medium.com/google-cloud/hosting-web-applications-on-google-cloud-an-overview-46f5605eb3a6)

[Deploy Web Applications Automatically Using GitHub Webhooks](https://www.toptal.com/devops/deploy-web-applications-automatically-using-github-webhooks)

[Turning a GitHub page into a Progressive Web App](https://christianheilmann.com/2022/01/13/turning-a-github-page-into-a-progressive-web-app/)

[Как оставаться в рамках Free Tier](https://www.infoworld.com/article/3585633/how-to-make-the-most-of-the-google-cloud-free-tier.html)
