import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers

from .forms import DonateForm, DepositForm
from .models import Donation, Deposit, Acceptation

# Create your views here.

@login_required
def donate(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            donation = form.save(commit=False)
            donation.donator = request.user  # Assuming the currently logged-in user is the donator
            donation.save()
            return redirect(reverse('caps:deposits', kwargs={'donation_id': donation.id}))  # Redirect to a page to display donations
    else:
        form = DonateForm()

    context = {
        'form': form,
    }

    return render(request, 'caps/donate.html', context)


@login_required
def add_deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.owner = request.user
            deposit.save()
            return redirect('accounts:dashboard')
    else:
        form = DepositForm()

    context = {
        'form': form,
    }

    return render(request, 'caps/add_deposit.html', context)


@login_required
def deposits(request, donation_id):
    donation = Donation.objects.get(id=donation_id)

    if donation.donator != request.user:
        return redirect('accounts:dashboard')

    deposits = Deposit.objects.exclude(owner=request.user, active=False)

    deposits_json = serializers.serialize('json', deposits)
    deposits_data = json.loads(deposits_json)

    context = {
        'deposits': deposits,
        'deposits_data': deposits_json,
        'donation': donation,
    }

    return render(request, 'caps/deposits.html', context)


@login_required
def wait_for_vol(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    donation.wait_for_vol = True
    donation.save()

    return redirect(reverse('caps:deposits', kwargs={'donation_id': donation.id}))

@login_required
def not_wait_for_vol(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    donation.wait_for_vol = False
    donation.save()

    return redirect(reverse('caps:deposits', kwargs={'donation_id': donation.id}))


@login_required
def donations(request):
    donations = Donation.objects.exclude(donator=request.user, donated=True)
    donations_json = serializers.serialize('json', donations)

    context = {
        'donations': donations,
        'donations_data': donations_json,
    }
    return render(request, 'caps/donations.html', context)


@login_required
def donation_approval(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    Acceptation.objects.create(volunteer=request.user, donation=donation)

    return render(request, 'caps/donation_approval.html')


@login_required
def deposit_approval(request, deposit_id, acceptation_id):
    deposit = Deposit.objects.get(id=deposit_id)
    acceptation = Acceptation.objects.get(id=acceptation_id)
    acceptation.deposit = deposit
    acceptation.save()

    return render(request, 'caps/deposit_approval.html')


@login_required
def notifications(request):
    notifs_data = []

    # notifications = Acceptation.objects.filter(donation__donator=request.user, donation_accepted=False, donation_rejected=False)
    notifications = Acceptation.objects.all()


    # notifications = Acceptation.objects.exclude(donation__donator=request.user, donation_accepted=False, donation_rejected=True)
    for notif in notifications:
        if notif.donation.donator == request.user and notif.donation_accepted == False and notif.donation_rejected == False:
            notifs_data.append({
                'text': 'volunteer_requested',
                'main': notif
            })

        elif notif.donation.donator != request.user and notif.donation_accepted == True and notif.donation_rejected == False and notif.deposit == None:
            notifs_data.append({
                'text': 'request_accepted',
                'main': notif
            })

        if notif.deposit != None:
            if notif.donation.donator != request.user and notif.deposit.owner == request.user and notif.deposit_accepted == False and notif.deposit_rejected == False and notif.deposit != None:
                notifs_data.append({
                    'text': 'deposit_requested',
                    'main': notif
                })

            elif notif.donation.donator != request.user and notif.deposit.owner != request.user and notif.donation_accepted == True and notif.donation_rejected == False and notif.deposit_accepted == True:
                notifs_data.append({
                    'text': 'deposit_accepted',
                    'main': notif
                })

    context = {
        'notifications': notifs_data,
    }

    return render(request, 'caps/notifications.html', context)


@login_required
def donation_accept(request, acceptation_id):
    acceptation = Acceptation.objects.get(id=acceptation_id)

    if acceptation.donation.donator != request.user:
        return redirect('caps:notifications')
        
    acceptation.donation_accepted = True
    acceptation.save()
    
    return redirect('caps:notifications')


@login_required
def donation_reject(request, acceptation_id):
    acceptation = Acceptation.objects.get(id=acceptation_id)

    if acceptation.donation.donator != request.user:
        return redirect('caps:notifications')

    acceptation.donation_rejected = True
    acceptation.save()
    
    return redirect('caps:notifications')


@login_required
def deposit_accept(request, acceptation_id):
    acceptation = Acceptation.objects.get(id=acceptation_id)

    if acceptation.deposit.owner != request.user:
        return redirect('caps:notifications')
        
    acceptation.deposit_accepted = True
    acceptation.save()

    donation = acceptation.donation
    donation.donated = True
    donation.save()
    
    return redirect('caps:notifications')


@login_required
def deposit_reject(request, acceptation_id):
    acceptation = Acceptation.objects.get(id=acceptation_id)

    if acceptation.deposit.owner != request.user:
        return redirect('caps:notifications')

    acceptation.deposit_rejected = True
    acceptation.save()
    
    return redirect('caps:notifications')


@login_required
def choose_deposit(request, acceptation_id):
    acceptation = Acceptation.objects.get(id=acceptation_id)
    deposits = Deposit.objects.exclude(owner=request.user)

    deposits_data = []

    for deposit in deposits:
        if deposit.capacity >= acceptation.donation.quantity:
            deposits_data.append(deposit)

    context = {
        'deposits': deposits_data,
        'acceptation': acceptation,
        'deposits_data': serializers.serialize('json', deposits_data),
    }

    return render(request, 'caps/choose_deposit.html', context)



@login_required
def my_donations(request):
    donations = Donation.objects.filter(donator=request.user)

    context = {
        'donations': donations,
    }

    return render(request, 'caps/my_donations.html', context)


@login_required
def donation(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    if donation.donator != request.user:
        return redirect('accounts:dashboard')

    context = {
        'donation': donation,
    }

    return render(request, 'caps/donation.html', context)


@login_required
def my_deposits(request):
    deposits = Deposit.objects.filter(owner=request.user)

    context = {
        'deposits': deposits,
    }

    return render(request, 'caps/my_deposits.html', context)


@login_required
def deposit(request, deposit_id):
    deposit = Deposit.objects.get(id=deposit_id)
    if deposit.owner != request.user:
        return redirect('accounts:dashboard')

    context = {
        'deposit': deposit,
    }

    return render(request, 'caps/deposit.html', context)