from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect


class NewPerson(View):
    def get(self, request):
        return render(request, "new_person.html")

    def post(self, request):
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        #image = request.POST.get('image')
        new_person = Person.objects.create(name=f'{name}', last_name=f'{last_name}', description=f'{description}')
        msg = "Dodano nową osobę"
        return render(request, "base.html", locals())


class NewGroup(View):
    def get(self, request):
        return render(request, "new_group.html")

    def post(self, request):
        name = request.POST.get('name')
        new_group = Group.objects.create(name=name)
        msg = "Dodano nową grupę"
        return render(request, "base.html", locals())


class Modify(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        cnx = {
            "name": person.name,
            "last_name": person.last_name,
            "description": person.description,
            "id": person.id,
        }
        return render(request, "modify_person.html", cnx)

    def post(self, request, id):
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        # image = request.POST.get('image')
        new_person = Person.objects.get(pk=id)
        new_person.name = name
        new_person.last_name = last_name
        new_person.description = description
        new_person.save()
        return HttpResponseRedirect(f'/show/{id}')


class AddAddress(View):
    def post(self, request, id):
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_no = request.POST.get('house_no')
        flat_no = request.POST.get('flat_no')
        new_address = Address.objects.create\
            (city=f'{city}', street=f'{street}', house_no=f'{house_no}', flat_no=f'{flat_no}')
        contact = Person.objects.get(pk=id)
        contact.adres = new_address
        contact.save()
        people = Person.objects.all()
        return HttpResponseRedirect("/")


class AddEmail(View):
    def post(self, request, id):
        email_address = request.POST.get('email_address')
        email_type = request.POST.get('email_type')
        contact = Person.objects.get(pk=id)
        new_address = Email()
        new_address.email_address = email_address
        new_address.email_type = email_type
        new_address.e_owner = contact
        new_address.save()
        people = Person.objects.all()
        return HttpResponseRedirect("/")


class AddPhone(View):
    def post(self, request, id):
        ph_number = request.POST.get('ph_number')
        ph_type = request.POST.get('ph_type')
        contact = Person.objects.get(id=id)
        new_phone = Phone()
        new_phone.ph_number = ph_number
        new_phone.ph_type = ph_type
        new_phone.owner = contact
        new_phone.save()
        people = Person.objects.all()
        return HttpResponseRedirect("/")


class Delete(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        person.delete()
        return HttpResponseRedirect('/')


class Single(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        cnx = {
            "name": person.name,
            "last_name": person.last_name,
            "description": person.description,
            "address": person.adres,
            "id": person.id,
            "phone": person.phone_set.all(),
            "email": person.email_set.all(),
        }
        return render(request, "single.html", cnx)


class Groups(View):
    def get(self, request, id):
        show_group = Group.objects.get(pk=id)
        cnx = {
            "name": show_group.name,
            "person": show_group.persons.all(),
        }
        return render(request, "show_group.html", cnx)


class AddMember(View):
    def get(self, request, id):
        groups = Group.objects.all()
        return render(request, "add_member.html", locals())

    def post(self, request, id):
        name = request.POST.getlist('name')
        member = Person.objects.get(pk=id)
        for g_id in name:
            i = Group.objects.get(id=int(g_id))
            i.persons.add(member)
        people = Person.objects.all()
        msg = "Dodano"
        return render(request, "base.html", locals())


class GroupList(View):
    def get(self, request):
        group = Group.objects.all()
        return render(request, "group_list.html", locals())

    def post(self, request):
        search = request.POST.get('search')
        data = search.split()
        l_data = [x.lower() for x in data]
        person = Person.objects.all()
        group = Group.objects.all()
        person_list = []
        res = []
        for d in l_data:
            for p in person:
                if d == p.name.lower() or d == p.last_name.lower():
                    person_list.append(p)
        for g in group:
            for a in g.persons.all():
                for p in person_list:
                    if p == a:
                        if g not in res:
                            res.append(g)
        group = res
        return render(request, "search.html", locals())


class Basic(View):
    def get(self, request):
        people = Person.objects.all().order_by('last_name')
        return render(request, "person.html", locals())