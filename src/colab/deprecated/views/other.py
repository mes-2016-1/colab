#!/usr/bin/env python
# encoding: utf-8
"""
other.py

Created by Sergio Campos on 2012-01-10.
"""

import datetime

from django.template import RequestContext
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.utils import timezone
from django.utils.translation import ugettext as _

from haystack.query import SearchQuerySet

from super_archives import queries


def home(request):
    """Index page view"""

    latest_threads = queries.get_latest_threads()
    hottest_threads = queries.get_hottest_threads()

    count_types = {}
    six_months = timezone.now() - datetime.timedelta(days=180)
    for type in ['wiki', 'thread', 'changeset', 'ticket']:
        count_types[type] = SearchQuerySet().filter(
            type=type,
            modified__gte=six_months,
        ).count()

    template_data = {
        'hottest_threads': hottest_threads[:6],
        'latest_threads': latest_threads[:6],
        'type_count': count_types,
        'latest_results': SearchQuerySet().all().order_by(
            '-modified', '-created'
        )[:6],
    }
    return render_to_response('home.html', template_data,
                              context_instance=RequestContext(request))


def search(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    query = request.GET.get('q')
    sort = request.GET.get('o')
    type_ = request.GET.get('type')
    try:
        page_number = int(request.GET.get('p', '1'))
    except ValueError:
        page_number = 1

    try:
        results_per_page = int(request.GET.get('per_page', 16))
    except ValueError:
        results_per_page = 16

    filters = {
        'Type': type_,
    }

    query = solrutils.build_query(query, filters)

    # Query Solr for results
    solr_dict_resp = solrutils.select(query, results_per_page,
                                      page_number, sort)

    docs = solrutils.SolrPaginator(solr_dict_resp, page_number)

    template_data = {
        'docs': docs,
        'anonymous': _(u'anônimo'),
        'q': query,
        'type': type_,
    }

    return render_to_response('search.html', template_data,
                              RequestContext(request))
